import numpy as np
import os
from PIL import Image

class DatasetLoader(object):

    def __init__(self, input_path, label_path):
        '''
        This is the Base DatasetLoader class

        INPUTS:
        - train_path : The path to the directory holding the training data
        - trainanot_path : The path to the directory holding the label data
        '''
        
        self.input_path = input_path
        self.label_path = label_path

        # Check if the path names ends in '/'
        if self.input_path[-1] != '/':
            self.input_path += '/'
        if self.label_path[-1] != '/':
            self.label_path += '/'

        self.input_names = np.array(os.listdir(input_path))
        self.label_names = np.array(os.listdir(label_path))

        self.total_inputs = len(self.input_names)
        self.total_labels = len(self.label_names)
        
        # Make sure there are same number of inputs as the number of labels
        assert (self.total_inputs == self.total_labels)

    def show_paths(self):
        '''
        The method to show the input path

        Arguments:
        None

        Returns:
        - str = The input path
        - str = The label path
        '''

        return self.input_path, self.label_path

    def glowhigh(self, batch_size=1, return_range=True):
        if batch_size > self.total_inputs:
            raise RuntimeError('Batch size is greater than the total number of files present!!')

        oidx = np.random.randint(0, self.total_inputs, size=1)
        sidx = oidx + batch_size

        if sidx >= self.total_inputs:
            sidx = oidx
            oidx = sidx - batch_size
        
        if return_range:
            return np.arange(start=oidx, 
                             stop=sidx)

        return oidx, sidx

    def get_batch(self, batch_size):
        pass

    def create_loader(self):
        pass
