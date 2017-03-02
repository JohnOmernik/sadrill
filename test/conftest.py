from sqlalchemy.dialects import registry

registry.register("drill", "sqlalchemy_drill.sadrill", "DrillDialect_sadrill")
registry.register("drill.sadrill", "sqlalchemy_drill.sadrill", "DrillDialect_sadrill")

from sqlalchemy.testing.plugin.pytestplugin import *
