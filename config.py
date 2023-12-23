import argparse
def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ds', type=int, default=0, help='dataset id')
    parser.add_argument("--time_no_agg", action="store_true", default=False, help="Not aggregate time feature")
    parser.add_argument("--train_anyway", action="store_true", default=False, help="training over again")
    parser.add_argument("--filename", type=str, default='/', help="filename")
    parser.add_argument("--layers", type=int, default=2, help="layers")
    parser.add_argument("--gw_beta", type=float, default=10, help="gw_beta")
    parser.add_argument("--gw_epoch", type=int, default=6000, help="gw_epoch")
    parser.add_argument("--step_size", type=int, default=1, help="step_size")
    parser.add_argument("--translate", action="store_true", default=True, help="training over again")
    parser.add_argument("--unsup", type=int, default=1)
    global_args = parser.parse_args()
    print('IMPORTANT! current ARGs are', global_args)

    return global_args
