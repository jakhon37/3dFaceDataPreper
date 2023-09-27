
import pyvista as pv
import os
import numpy as np
import trimesh

def rescale_tofalme2(inObjPath, outObjPath):
    # Load the original mesh
    mesh = pv.read(inObjPath)
    # Decimate the mesh
    decimated_mesh = mesh.decimate(target_reduction=1.0 - (9958 / mesh.n_faces))
    # Save the decimated mesh
    decimated_mesh.save(outObjPath)

root = os.path.abspath(os.getcwd())
parent_root = os.path.abspath(os.path.join(root, os.pardir))
print('\n\n|------------- parent_root:', parent_root)
obj_in = os.path.join(parent_root, "example/nrm_n07.obj")
obj_out = os.path.join(parent_root, "example/nrm_n07_scaled.ply")
rescale_tofalme2(obj_in, obj_out)
print('\n\n|------------- obj_out:', obj_out)
