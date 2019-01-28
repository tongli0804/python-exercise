
class Rule():
    def action(self,bolck, handler):
        handler.start(self.type)
        handler.feed(bolck)
        handler.end(self.type)
        return.True