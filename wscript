def options(opt):
    opt.load('compiler_cxx')


def configure(conf):
  conf.env.CXXFLAGS += ['-O2', '-Wall', '-g', '-pipe']
  conf.check_cfg(package = 'pficommon', args = '--cflags --libs')
  conf.load('compiler_cxx')

def build(bld):
  bld.program(
    source = 'ml_update.cpp',
    target = 'ml_update',
    use = 'PFICOMMON',
    )

  bld.program(
    source = 'ml_analysis.cpp',
    target = 'ml_analysis',
    use = 'PFICOMMON',
    )

