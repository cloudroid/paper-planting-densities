"""
Plot the synthetic data and model as well as the inversion results.
"""
import sys
import cPickle as pickle
import numpy
from fatiando import vis
from fatiando.mesher.volume import extract, vfilter
pyplot = vis.pyplot

with open(sys.argv[1]) as f:
    model = pickle.load(f)

def setview(s):
    s.scene.camera.position = [-2263.7301544182874, 488.95715870190594, 318.19750997028473]
    s.scene.camera.focal_point = [490.77486582744939, 489.04595996051546, 562.78867616870843]
    s.scene.camera.view_angle = 30.0
    s.scene.camera.view_up = [0.088448540522960639, -0.0026066904949591562, -0.99607733677863675]
    s.scene.camera.clipping_range = [1662.1503239591332, 4168.9269870750722]
    s.scene.camera.compute_view_plane_normal()
    s.scene.render()

extent = [0, 1000, 0, 1000, 0, 1000]
fmt = 'png'

f = vis.mayavi_figure(size=(900,900))
p = vis.prisms3D(model, extract('density', model), vmin=0, vmax=2000,
    cmap='gist_yarg')
a = vis.add_axes3d(vis.add_outline3d(extent), ranges=[i*0.001 for i in extent],
    fmt='%.1f', nlabels=3)
a.axes.x_label, a.axes.y_label, a.axes.z_label = '', '', ''
a.axes.font_factor = 2
vis.wall_north(extent)
vis.wall_bottom(extent)
setview(f)
vis.mlab.savefig('.'.join(['model', fmt]))


vis.mlab.show()
