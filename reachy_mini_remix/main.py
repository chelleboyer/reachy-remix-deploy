"""Main entry point for Reachy Mini App system.

This module contains the ReachyRemix class that integrates with the Reachy Mini
App system through the ReachyMiniApp interface.
"""

import threading
import traceback
from reachy_mini import ReachyMini, ReachyMiniApp


class ReachyMiniRemix(ReachyMiniApp):
    """Reachy Mini App wrapper for Reachy Remix.
    
    Gradio-based motion builder interface.
    The Reachy Mini system will automatically detect the Gradio port.
    """
    
    # This will be set dynamically after Gradio launches
    custom_app_url: str | None = None
    
    def run(self, reachy_mini: ReachyMini, stop_event: threading.Event):
        """Run the Reachy Remix Gradio app.
        
        Args:
            reachy_mini: The ReachyMini instance provided by the dashboard
            stop_event: Threading event to signal when the app should stop
        """
        import sys
        import logging
        import time
        
        # CRITICAL: Test if run() is even being called
        with open("/tmp/reachy-remix-debug.log", "w") as f:
            f.write("RUN METHOD CALLED!\n")
            f.flush()
        
        # Set up logging to help debug
        logging.basicConfig(level=logging.INFO, force=True)
        logger = logging.getLogger(__name__)
        
        logger.info("=" * 60)
        logger.info("REACHY REMIX APP STARTING")
        logger.info("=" * 60)
        
        try:
            # Import create_app here to avoid slow module loading at startup
            logger.info("Importing create_app...")
            from .app import create_app
            
            # Create Gradio app with the provided reachy_mini instance
            logger.info("Creating Gradio app with robot connection...")
            app = create_app(robot=reachy_mini, controller=None)
            logger.info("Gradio app created successfully")
            
            # Set up a way to stop Gradio when stop_event is set
            def check_stop_event():
                if stop_event.is_set():
                    print("Stop event detected, closing Gradio...")
                    app.close()
            
            # Monitor stop_event in a separate thread
            monitor_thread = threading.Thread(
                target=lambda: (stop_event.wait(), check_stop_event()),
                daemon=True
            )
            monitor_thread.start()
            
            logger.info("Setting up Gradio queue...")
            app.queue()  # Enable queue for better concurrency
            
            logger.info("Launching Gradio server (port will be auto-assigned)...")
            
            # Launch Gradio with prevent_thread_lock=True so it runs in background
            # Let Gradio auto-assign an available port (starts from 7860)
            # NOTE: With prevent_thread_lock=True, launch() returns the App object, not a tuple
            app.launch(
                server_name="0.0.0.0",
                share=False,
                prevent_thread_lock=True,  # Don't block - run in background
                show_error=True,
                quiet=False,
                inbrowser=False,
            )
            
            # Get the actual local URL from the app's server
            # Gradio stores it in app.local_url after launch
            local_url = app.local_url if hasattr(app, 'local_url') else "http://localhost:7860"
            
            # Update the class property with the actual URL for the gear icon
            # Convert 0.0.0.0 to localhost for browser compatibility
            self.custom_app_url = local_url.replace("0.0.0.0", "localhost")
            type(self).custom_app_url = self.custom_app_url  # Update class attribute too
            
            logger.info("=" * 60)
            logger.info(f"Gradio server running at: {local_url}")
            logger.info(f"Dashboard gear icon (⚙️) will link to: {self.custom_app_url}")
            logger.info("=" * 60)
            
            # Keep the app running until stop_event is set
            logger.info("App is running. Waiting for stop signal...")
            
            # Use a while loop like the documentation shows, not stop_event.wait()
            import time
            while not stop_event.is_set():
                time.sleep(0.1)
            
            logger.info("Stop signal received, shutting down Gradio server...")
            app.close()
            logger.info("Gradio server has shut down")
            
        except Exception as e:
            logger.error("=" * 60)
            logger.error(f"FATAL ERROR in Reachy Remix: {e}")
            logger.error("=" * 60)
            logger.exception("Full traceback:")
            raise
        finally:
            logger.info("=" * 60)
            logger.info("REACHY REMIX APP EXITING")
            logger.info("=" * 60)
