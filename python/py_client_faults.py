'''
//Copyright [2016] [SnapRoute Inc]
//
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
//       Unless required by applicable law or agreed to in writing, software
//       distributed under the License is distributed on an "AS IS" BASIS,
//       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//       See the License for the specific language governing permissions and
//       limitations under the License.
//
// _______  __       __________   ___      _______.____    __    ____  __  .___________.  ______  __    __
// |   ____||  |     |   ____\  \ /  /     /       |\   \  /  \  /   / |  | |           | /      ||  |  |  |
// |  |__   |  |     |  |__   \  V  /     |   (----` \   \/    \/   /  |  | `---|  |----`|  ,----'|  |__|  |
// |   __|  |  |     |   __|   >   <       \   \      \            /   |  |     |  |     |  |     |   __   |
// |  |     |  `----.|  |____ /  .  \  .----)   |      \    /\    /    |  |     |  |     |  `----.|  |  |  |
// |__|     |_______||_______/__/ \__\ |_______/        \__/  \__/     |__|     |__|      \______||__|  |__|
'''

'''
Websocket Client Example for Faults Published using Flexswitch
'''

import websocket
import sys
import getopt

def on_message(ws, message):
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"


if __name__ == "__main__":
    switchIp = "localhost"
    port = "8081"
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hs:p:",["switch-ip=","port="])
    except getopt.GetoptError:
        print 'py_client_faults.py -s <Switch IP> -p <Websocket-Port>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'py_client_faults.py -s <Switch IP> -p <Websocket-Port>'
            sys.exit()
        elif opt in ("-s", "--switch-ip"):
            switchIp = arg
        elif opt in ("-p", "--port"):
            port = arg

    websocket.enableTrace(True)
    addr = "ws://" + switchIp + ":" + port + "/faults"
    print addr
    ws = websocket.WebSocketApp(addr,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.run_forever()
