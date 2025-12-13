"""Main entry point for Reachy Mini App system.

This module contains the ReachyRemix class that integrates with the Reachy Mini
App system through the ReachyMiniApp interface.
"""

import threading
import traceback
from reachy_mini import ReachyMini, ReachyMiniApp
from .app import create_app


class ReachyMiniRemix(ReachyMiniApp):
    """Reachy Mini App wrapper for Reachy Remix.
    
    Gradio-based motion builder interface.
    The Reachy Mini system will automatically detect the Gradio port.
    """
    
    def run(self, reachy_mini: ReachyMini, stop_event: threading.Event):
        """Run the Reachy Remix Gradio app.
        
        Args:
            reachy_mini: The ReachyMini instance provided by the dashboard
            stop_event: Threading event to signal when the app should stop
        """
        print("Starting Reachy Remix - Motion Builder")
        
        try:
            # Create Gradio app with the provided reachy_mini instance
            print("Creating Gradio app with robot connection...")
            app = create_app(robot=reachy_mini, controller=None)
            print("Gradio app created with robot connection")
            
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
            # Let Gradio auto-assign port by not specifying server_port
            local_url, share_url, _ = app.launch(
                server_name="0.0.0.0",
                share=False,
                prevent_thread_lock=True,  # Don't block - run in background
                show_error=True,
                quiet=False,
                inbrowser=False,
            )
            
            print("=" * 60)
            print(f"Gradio server running at: {local_url}")
            print(f"The Reachy Mini Dashboard will automatically detect this port")
            print("=" * 60)
            
            # Now wait for stop_event instead of blocking on launch
            stop_event.wait()
            
            print("Stopping Gradio server...")
            app.close()
            print("Gradio server has shut down")
            
        except Exception as e:
            print(f"ERROR: Fatal error in Reachy Remix: {e}")
            traceback.print_exc()
            raise
