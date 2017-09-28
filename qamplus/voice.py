
class VoiceClient(object):


    def __init__(self, base_obj):
        self.base_obj = base_obj
        self.api_resource = "/voice/v1/{}"

    def create(self,
               direction,
               to,
               caller_id,
               execution_logic,
               reference_logic='',
               country_iso2='us',
               technology='pstn' ):

        api_resource = self.api_resource.format(direction)
        return self.base_obj.post(api_resource=api_resource, direction=direction, to=to,
            caller_id=caller_id, execution_logic=execution_logic, reference_logic=reference_logic,
            country_iso2=country_iso2, technology=technology)


    def update(self):
        pass

    def delete(self):
        pass

    def get_status(self):
        pass


