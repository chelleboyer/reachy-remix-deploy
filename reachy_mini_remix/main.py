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
        import os
        
        # Force unbuffered output
        sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)
        sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', buffering=1)
        
        print("=" * 60, flush=True)
        print("REACHY REMIX APP STARTING", flush=True)
        print("=" * 60, flush=True)
        
        try:
            # Import create_app here to avoid slow module loading at startup
            from .app import create_app
            
            # Create Gradio app with the provided reachy_mini instance
            print("Creating Gradio app with robot connection...", flush=True)
            app = create_app(robot=reachy_mini, controller=None)
            print("Gradio app created with robot connection", flush=True)
            
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
            
            # Let Gradio find an available port automatically (starting from 7860)
            port = None
            
            print("=" * 60)
            print(f"Launching Gradio server (port will be assigned automatically)...")
            print("=" * 60)
            
            app.queue()  # Enable queue for better concurrency
            
            # Launch Gradio with prevent_thread_lock=True so it runs in background
            # Let Gradio auto-assign an available port (starts from 7860)
            local_url, share_url, _ = app.launch(
                server_name="0.0.0.0",
                share=False,
                prevent_thread_lock=True,  # Don't block - run in background
                show_error=True,
                quiet=False,
                inbrowser=False,
            )
            
            # Update the class property with the actual URL for the gear icon
            # Convert 0.0.0.0 to localhost for browser compatibility
            self.custom_app_url = local_url.replace("0.0.0.0", "localhost")
            type(self).custom_app_url = self.custom_app_url  # Update class attribute too
            
            print("=" * 60, flush=True)
            print(f"Gradio server running at: {local_url}", flush=True)
            print(f"Dashboard gear icon (⚙️) will link to: {self.custom_app_url}", flush=True)
            print("=" * 60, flush=True)
            
            # Keep the app running until stop_event is set
            print("Waiting for stop signal...", flush=True)
            stop_event.wait()
            
            print("Stop signal received, shutting down Gradio server...", flush=True)
            app.close()
            print("Gradio server has shut down", flush=True)
            
        except Exception as e:
            print("=" * 60, flush=True)
            print(f"ERROR: Fatal error in Reachy Remix: {e}", flush=True)
            print("=" * 60, flush=True)
            traceback.print_exc()
            sys.stdout.flush()
            sys.stderr.flush()
            raise
        finally:
            print("=" * 60, flush=True)
            print("REACHY REMIX APP EXITING", flush=True)
            print("=" * 60, flush=True)
