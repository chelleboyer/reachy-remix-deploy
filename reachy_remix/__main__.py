"""Entry point for running Reachy Remix as a module."""

from reachy_remix.app import create_app

if __name__ == "__main__":
    import sys
    
    print("🎵 Reachy Remix - Motion Builder")
    print("=" * 50)
    print("Running in standalone mode")
    print("⚠️  For Reachy Mini app system, use the Dashboard")
    print("=" * 50)
    
    # Initialize robot connection (optional)
    robot = None
    controller = None
    
    try:
        from reachy_mini.motion.recorded_move import RecordedMoves
        SDK_AVAILABLE = True
    except ImportError:
        print("⚠️  Reachy SDK not available - running in demo mode")
        SDK_AVAILABLE = False
    
    if SDK_AVAILABLE:
        print("Reachy SDK available - checking for robot connection...")
        try:
            from reachy_mini import ReachyMini
            robot = ReachyMini()
            print("✅ Robot connected!")
        except Exception as e:
            print(f"⚠️  Robot not available: {e}")
            print("Running in DEMO mode")
            robot = None
    else:
        print("Running in DEMO mode (SDK not installed)")
    
    print("=" * 50)
    print(f"Mode: {'ROBOT' if robot else 'DEMO'}")
    print("=" * 50)
    
    # Create app with robot connection
    app = create_app(robot=robot, controller=controller)
    
    # Launch Gradio app (auto-assign port in standalone mode)
    app.launch(
        server_name="0.0.0.0",  # Accessible on network
        share=False,  # Local only for security
        inbrowser=True,  # Auto-open browser
        show_error=True,
    )
