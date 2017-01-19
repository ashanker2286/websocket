RM=rm -f
RMFORCE=rm -rf
all: client_alarms client_events client_faults

client_events: client_events.go
	go build client_events.go

client_faults: client_faults.go
	go build client_faults.go

client_alarms: client_alarms.go
	go build client_alarms.go

clean:
	$(RM) client_alarms client_events client_faults
