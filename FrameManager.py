class FrameManager:
    def __init__(self, parent, processor):
        self.parent = parent
        self.processor = processor
        self.frames = {}

        # Create frames
        # self.frames["Merge"] = MergeFrame(parent, processor)
        # self.frames["ExtractText"] = ExtractTextFrame(parent, processor)

        self.current_frame = None
        # self.show_frame = "Merge"
