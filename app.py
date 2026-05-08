from tools.PushoverService import PushoverService

if __name__ == "__main__":

    svc = PushoverService()


    svc.tools["record_contact_requested"]["function"]("testing")