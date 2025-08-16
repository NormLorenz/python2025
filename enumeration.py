from enum import Enum

class State(Enum):
    '''Enumeration for different states of a process.'''
    STARTED = 'started'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    FAILED = 'failed'   

state: State = State.STARTED

if state == State.STARTED:
    print('Process has started.')
elif state == State.IN_PROGRESS:
    print('Process is in progress.')
elif state == State.COMPLETED:
    print('Process has completed successfully.')
elif state == State.FAILED:
    print('Process has failed.')
else:
    print('Unknown state.')

print(f'Current state: {state} - {state.name} - {state.value} {State("started")}')