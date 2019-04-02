import argparse

from train_setup import train

parser = argparse.ArgumentParser(description='Run training')

default_ds = "omniglot"
default_split = "vinyals"
default_train_way = 50
default_n_support = 5
default_n_query = 5
default_train_episodes = 2

# data
parser.add_argument("--data.dataset", type=str, default=default_ds,
                    help=f"dataset name (default: {default_ds}")
parser.add_argument("--data.split", type=str, default=default_split,
                    help=f"splitting name (default: {default_split}")
parser.add_argument("--data.train_way", type=int, default=default_train_way,
                    help=f"number of support classes: (default: {default_train_way})")
parser.add_argument("--data.train_n_support", type=int, default=default_n_support,
                    help=f"number of support examples per class (default: {default_n_support})")
parser.add_argument("--data.train_n_query", type=int, default=default_n_query,
                    help=f"number of query examples per class (default: {default_n_query})")
parser.add_argument("--data.train_episodes", type=int, default=default_train_episodes,
                    help=f"number of train episodes per epoch (default: {default_train_episodes})")
parser.add_argument("--data.cuda", action='store_true',
                    help=f"Train on GPU (default: False)")

# model
default_input = "28,28,1"
parser.add_argument("--model.x_dim", type=str, default=default_input,
                    help=f"dimensionality of input shapes (default: {default_input})")
parser.add_argument("--model.z_dim", type=int, default=64,
                    help="dimensionality of input ")

# training
default_epochs = 2
default_optim = 'Adam'
default_lr = 0.001
default_decay_every = 20
default_weight_decay = 0.0
default_patience = 10

parser.add_argument('--train.epochs', type=int, default=default_epochs,
                    help=f"number of epochs (default: {default_epochs})")
parser.add_argument('--train.optim_method', type=str, default=default_optim,
                    help=f"optimizator (default: {default_optim})")
parser.add_argument("--train.lr", type=float, default=default_lr,
                    help=f"learning rate (default: {default_lr})")
parser.add_argument("--train.patience", type=int, default=default_patience,
                    help=f"number of non-improving epochs after which training stops (default: {default_patience})")
parser.add_argument("--train.model_path", type=str, default="./model.h5",
                    help="Path to the saved model (default: ./model.h5)")

# Run training
args = vars(parser.parse_args())
train(args)