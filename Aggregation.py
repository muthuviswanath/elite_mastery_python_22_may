class Phone:
    def display(self,p):
        print(p.processor_model)

class Processor:
    
    def  __init__(self) -> None:
        self.processor_model = "i9"

processor = Processor()
ph = Phone()
ph.display(processor)
del  ph
print(processor.processor_model)