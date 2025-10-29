import pjsua as pj
import threading

# Placeholder SIP client for Callcentric using pjsua
# This code registers a SIP account with Callcentric and listens for incoming calls.
# When a call is received, you would integrate your ASR/LLM/TTS pipeline here.

SIP_DOMAIN = "callcentric.com"
SIP_USERNAME = "17778829020"  # your Callcentric SIP username
SIP_PASSWORD = "Zakaria15?"    # your SIP password
SIP_PROXY = "sip.callcentric.com"


class MyAccountCallback(pj.AccountCallback):
    def __init__(self, account):
        pj.AccountCallback.__init__(self, account)

    def on_incoming_call(self, call):
        print("Incoming call from", call.info().remote_uri)
        call.answer(200)
        # Here you would connect the call's audio media to your ASR/LLM/TTS pipeline
        # using a streaming interface (not implemented in this placeholder).
        print("Call answered, but no media handling is implemented.")


def main():
    # Create and initialize pjsua library
    lib = pj.Lib()
    try:
        lib.init(log_cfg=pj.LogConfig(level=3, callback=lambda level, str, len: print(str.strip())))
        # Create UDP transport which listens to any available port
        transport = lib.create_transport(pj.TransportType.UDP, pj.TransportConfig(0))
        lib.start()

        # Create account configuration
        acc_cfg = pj.AccountConfig(domain=SIP_DOMAIN, username=SIP_USERNAME, password=SIP_PASSWORD)
        acc_cfg.id = f"sip:{SIP_USERNAME}@{SIP_DOMAIN}"
        acc_cfg.reg_uri = f"sip:{SIP_PROXY}"
        # Register account
        account = lib.create_account(acc_cfg)
        # Set callback to handle incoming calls
        acc_cb = MyAccountCallback(account)
        account.set_callback(acc_cb)
        print("SIP account registered. Waiting for calls...")
        # Keep the application running
        threading.Event().wait()
    except Exception as e:
        print("Exception: ", e)
    finally:
        lib.destroy()
        lib = None


if __name__ == "__main__":
    main()
