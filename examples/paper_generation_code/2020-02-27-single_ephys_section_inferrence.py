import os
from deepinterpolation.generic import JsonSaver, ClassLoader
import datetime

now = datetime.datetime.now()
run_uid = now.strftime("%Y_%m_%d_%H_%M")

generator_param = {}
inferrence_param = {}

generator_param["type"] = "generator"
generator_param["name"] = "EphysGenerator"
generator_param["pre_post_frame"] = 30
generator_param["pre_post_omission"] = 1

generator_param[
    "train_path"
] = "/Users/jeromel/Documents/Work documents/Allen Institute/Projects/Deep2P/examples/tiny_continuous.dat2"
generator_param["batch_size"] = 100
generator_param["start_frame"] = 0
generator_param["end_frame"] = -1
generator_param["randomize"] = 0


inferrence_param["type"] = "inferrence"
inferrence_param["name"] = "core_inferrence"
inferrence_param[
    "model_path"
] = "/Users/jeromel/Documents/Work documents/Allen Institute/Projects/Deep2P/examples/large_training/2020_02_29_15_28_unet_single_ephys_1024_mean_squared_error-1275.h5"
inferrence_param[
    "output_file"
] = "/Users/jeromel/Documents/Work documents/Allen Institute/Projects/Deep2P/examples/tiny_training/inferrence/tiny_continuous_unet_single_ephys_1024_nodropout_large.h5"

jobdir = "/Users/jeromel/Documents/Work documents/Allen Institute/Projects/Deep2P/examples/tiny_training/inferrence/"

try:
    os.mkdir(jobdir)
except:
    print("folder already exists")

path_generator = os.path.join(jobdir, "generator.json")
json_obj = JsonSaver(generator_param)
json_obj.save_json(path_generator)

path_infer = os.path.join(jobdir, "inferrence.json")
json_obj = JsonSaver(inferrence_param)
json_obj.save_json(path_infer)

generator_obj = ClassLoader(path_generator)
data_generator = generator_obj.find_and_build()(path_generator)

inferrence_obj = ClassLoader(path_infer)
inferrence_class = inferrence_obj.find_and_build()(path_infer, data_generator)


inferrence_class.run()
