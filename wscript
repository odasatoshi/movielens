def options(opt):
    opt.load('compiler_cxx')


def configure(conf):
  conf.env.CXXFLAGS += ['-O2', '-Wall', '-g', '-pipe']
  conf.load('compiler_cxx')
  conf.check_cfg(package = 'pficommon', args = '--cflags --libs')
  conf.check_cxx(lib = 'msgpack')

def build(bld):
  bld.program(
    source = 'ml_update.cpp',
    target = 'ml_update',
    use = 'PFICOMMON MSGPACK',
    )

  bld.program(
    source = 'ml_analysis.cpp',
    target = 'ml_analysis',
    use = 'PFICOMMON MSGPACK',
    )

