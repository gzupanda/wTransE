#import scipy.io
import efe
from efe.exp_generators import *
import efe.tools as tools

if __name__ =="__main__":
	#Load data, ensure that data is at path: 'path'/'name'/[train|valid|test].txt
	wn18exp = build_data(name = 'wn18',path = tools.cur_path + '/datasets/')
	#SGD hyper-parameters:
	params = Parameters(learning_rate = 0.02, 
						max_iter = 1000,
						batch_size = int(len(wn18exp.train.values) / 100),  #Make 100 batches
						neg_ratio = 1, 
						valid_scores_every = 1000,
						learning_rate_policy = 'adagrad',
						contiguous_sampling = False )

	all_params = { "wTransE_2L_Model" : params } ; emb_size = 200; lmbda = 2; params.miuA = 0.5;params.miuB = 0.5;params.lambda_A = 1;params.lambda_B = 1
	tools.logger.info("Max iter: " + str(params.max_iter))
	tools.logger.info("Generated negatives ratio: " + str(params.neg_ratio))
	tools.logger.info("Batch size: " + str(params.batch_size))
	tools.logger.info( "Learning rate: " + str(params.learning_rate))
	tools.logger.info("emb_size: " + str(emb_size))
	tools.logger.info("Margin: " + str(lmbda))
	tools.logger.info("miuA: " + str(params.miuA))
	tools.logger.info("miuB: " + str(params.miuB))
	tools.logger.info("lambda_A: " + str(params.lambda_A))
	tools.logger.info("lambda_B: " + str(params.lambda_B))
	#Then call a local grid search, here only with one value of rank and regularization
	wn18exp.grid_search_on_all_models(all_params, embedding_size_grid = [emb_size], lmbda_grid = [lmbda], nb_runs = 1)
	#Print best averaged metrics:
	wn18exp.print_best_MRR_and_hits()
	#Print best averaged metrics per relation:
	wn18exp.print_best_MRR_and_hits_per_rel()