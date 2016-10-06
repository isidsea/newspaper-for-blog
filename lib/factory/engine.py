from ..engine.generic import GenericEngine

class EngineFactory:
    GENERIC = 0
    
    def __init__(self):
        pass
    
    @classmethod
    def get_engine(self, engine_name=None):
        assert engine_name is not None, "engine_name is not defined."
        
        if engine_name == EngineFactory.GENERIC:
            return GenericEngine()