class usuario:
    def __init__(self, id, email, senha, perfil):
        self.id     = id
        self.email  = email
        self.senha  = senha
        self.perfil = perfil

class metas:
    def __init__(self, id, empreendimento, periodo, agrupamento_empreendimento, meta, fl_considera_bi, dt_insert, user):
        self.id                         = id
        self.empreendimento             = empreendimento
        self.periodo                    = periodo
        self.agrupamento_empreendimento = agrupamento_empreendimento
        self.meta                       = meta
        self.fl_considera_bi            = fl_considera_bi
        self.dt_insert                  = dt_insert
        self.user                       = user

class empreendimento_class:
    def __init__(self, id, empreendimento):
        self.id              = id
        self.empreendimento  = empreendimento