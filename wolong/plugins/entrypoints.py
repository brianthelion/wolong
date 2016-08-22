from plugnparse import entrypoint

def load_setargs(parser):
    parser.add_argument('load_bucket')

@entrypoint(['load'], args=load_setargs)
def cli_load(self, arg_ns, arg_parser):
    self.cursor = self.buckets[arg_ns.load_bucket]

def info_setargs(parser):
    parser.add_argument('info_bucket')

@entrypoint(['info'], args=info_setargs)
def cli_info(api, ns, parser):
    print(api._data_store)
    if not hasattr(ns, 'info_bucket'):
        return
    if ns.info_bucket is None:
        return
    if ns.info_bucket not in api.buckets:
        err_str = "{} not a valid bucket!"
        parser.error(err_s.format(ns.info_bucket))
    print(api.buckets[ns.info_bucket])

def save_setargs(parser):
    parser.add_argument('save_bucket')
    parser.add_argument('--overwrite', default=False, action='store_true')

@entrypoint(['save'], args=save_setargs)
def cli_save(api, ns, parser):
    if ns.save_bucket not in api.buckets or \
       (ns.save_bucket in api.buckets and ns.overwrite):
        api.buckets[ns.save_bucket] = api.cursor
    else:
        err_str = "Bucket {} already exists! Use --overwrite."
        parser.error(err_str.format(ns.save_bucket))
