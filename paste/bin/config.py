from paste import app


class Config:
    def __init__(self):
        self.dir_root = app.config['dir_root']
        self.local = None

        try:
            import settings
            self.local = {k.upper(): v for k, v in vars(settings).items()}

            for k, v in self.local.items():
                if k.startswith('_'):
                    continue

                app.config[k] = v
        except:
            pass