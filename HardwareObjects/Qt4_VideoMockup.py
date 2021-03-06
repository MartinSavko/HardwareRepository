#
#  Project: MXCuBE
#  https://github.com/mxcube.
#
#  This file is part of MXCuBE software.
#
#  MXCuBE is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  MXCuBE is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#  along with MXCuBE.  If not, see <http://www.gnu.org/licenses/>.

import os
import gevent
import numpy as np

from QtImport import QPixmap, QImage

from GenericVideoDevice import GenericVideoDevice


class Qt4_VideoMockup(GenericVideoDevice):
    """
    Descript. :
    """
    def __init__(self, name):
        """
        Descript. :
        """
        GenericVideoDevice.__init__(self, name)
        self.force_update = None
        self.image_type = None
        self.image = None

    def init(self):
        """
        Descript. :
        """ 
        current_path = os.path.dirname(os.path.abspath(__file__)).split(os.sep)
        current_path = os.path.join(*current_path[1:-1])
        image_path = self.getProperty('image_path', "/" + current_path + "/tests/fakeimg.jpg")
        self.image = QPixmap(image_path)
        self.image_dimensions = (self.image.width(), self.image.height())
        self.setIsReady(True)
        GenericVideoDevice.init(self)

    def get_image_dimensions(self):
        return self.image_dimensions

    def get_new_image(self):
        self.emit("imageReceived", self.image) 

    def save_snapshot(self, filename, image_type='PNG'):
        qimage = QImage(self.image)
        qimage.save(filename, image_type)

    def get_snapshot(self, bw=None, return_as_array=None):
        qimage = QImage(self.image)
        if return_as_array:
            qimage = qimage.convertToFormat(4)
            ptr = qimage.bits()
            ptr.setsize(qimage.byteCount())

            image_array = np.array(ptr).reshape(qimage.height(), qimage.width(), 4)
            if bw:
                return np.dot(image_array[...,:3], [0.299, 0.587, 0.144])
            else:
                return image_array
        else:
            if bw:
                return qimage.convertToFormat(QImage.Format_Mono)
            else:
                return qimage

    def get_contrast(self):
        return 34

    def set_contrast(self, contrast_value):
        return

    def get_brightness(self):
        return 54

    def set_brightness(self, brightness_value):
        return
  
    def get_gain(self):
        return 32
  
    def set_gain(self, gain_value):
        return

    def get_gamma(self):
        return 22

    def set_gamma(self, gamma_value):
        return

    def get_exposure_time(self):
        return 0.23

    def get_video_live(self):
        return True

    def get_width(self):
        return self.image.width()
    
    def getWidth(self):
        self.get_width()
    
    def get_height(self):
        return self.image.height()
    
    def getHeigth(self):
        self.get_height()
        