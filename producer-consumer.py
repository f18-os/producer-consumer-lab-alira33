from ExtractFrames import *
from ConvertToGrayscale import *


ExtractProducerThread().start()
ExtractConsumerThread().start()
GrayscaleProducerThread().start()
GrayscaleConsumerThread().start()
# jobs = []

# class ExecuteJobs():
#     def run(self):
#     # Create a list of jobs and then iterate through
#     # the number of processes appending each process to
#     # the job list
#         grayscale = multiprocessing.Process(target=GrayscaleProducerThread)
#         jobs.append(grayscale)
#         extract = multiprocessing.Process(target=ExtractProducerThread)
#         jobs.append(extract)
#         # Start the processes (i.e. calculate the random number lists)
#     for j in jobs:
#         j.start()

#         # Ensure all of the processes have finished
#     for j in jobs:
#         j.join()

#         print ("List processing complete.")

# ExecuteJobs()