"""Entry point for running Reachy Remix as a module.

This is for standalone testing outside of the Reachy Mini Dashboard.
For deployment, the app runs through the ReachyMiniApp interface via main.py
"""

from reachy_mini_remix.app import create_app

if __name__ == "__main__":
    import sys
    
    print("Reachy Remix - Motion Builder")
    print("=" * 50)
    print("Running in standalone mode")
    print("WARNING: For production use, install via Dashboard")
    print("=" * 50)
    
    # Initialize robot connection (optional)
    robot = None
    controller = None
    
    try:
        from reachy_mini.motion.recorded_move import RecordedMoves
        SDK_AVAILABLE = True
    except ImportError:
        print("WARNING: Reachy SDK not available - running in demo mode")
        SDK_AVAILABLE = False
    
    if SDK_AVAILABLE:
        print("Reachy SDK available - checking for robot connection...")
        try:
            from reachy_mini import ReachyMini
            robot = ReachyMini()
            print("Robot connected!")
        except Exception as e:
            print(f"WARNING: Robot not available: {e}")
            print("Running in DEMO mode")
            robot = None
    else:
        print("Running in DEMO mode (SDK not installed)")
    
    print("=" * 50)
    print(f"Mode: {'ROBOT' if robot else 'DEMO'}")
    print("=" * 50)
    
    # Create app with robot connection
    app = create_app(robot=robot, controller=controller)
    
    # Launch Gradio app (standalone mode)
    app.launch(
        server_name="0.0.0.0",  # Accessible on network
        share=False,  # Local only for security
        inbrowser=True,  # Auto-open browser
        show_error=True,
    )
