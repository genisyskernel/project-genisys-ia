# Class Center Screen Function #

class FrameCenter:

    # FUNCTIONS #
    def center(self, x, y):
        # Center screen #
        frame_width = int(self.master.winfo_screenwidth()/2 - (x/2))
        frame_height = int(self.master.winfo_screenheight()/2 - (y/2))
        self.master.geometry("{0}x{1}+{2}+{3}".format(x, y, frame_width, frame_height))
        #print("MONITOR - CONFIGS\nX: {0} / Y: {1} / WIDTH: {2} / HEIGHT: {3}".format(x, y, frame_width, frame_height))
