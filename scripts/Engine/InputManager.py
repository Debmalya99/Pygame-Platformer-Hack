import pygame

class InputManager:
    def __init__(self):
        self.action_map = {
            'ui_left':[pygame.K_LEFT,pygame.K_a],
            'ui_right':[pygame.K_RIGHT,pygame.K_d],
            'ui_up':[pygame.K_UP,pygame.K_w],
            'ui_down':[pygame.K_DOWN,pygame.K_s],
            'ui_jump':[pygame.K_SPACE],
            'ui_pause':[pygame.K_ESCAPE,pygame.K_x]
        }

        self.pressed = set()
        self.released = set()

    
    ## The following is_action_* functions are what you use to check if something is pressed or not
    def is_action_pressed(self,action_name):
        keys = pygame.key.get_pressed()

        return any(keys[k] for k in self.action_map[action_name])
    
    def is_action_just_pressed(self,action_name):
        return any(k in self.pressed for k in self.action_map[action_name])
    
    def is_action_just_released(self,action_name):
        return any(k in self.released for k in self.action_map[action_name])
    
    
    ## Call this function every frame once. Takes the list of events polled/queued as argument
    def capture_input(self,events):
        self.pressed.clear()
        self.released.clear()

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.pressed.add(event.key)
            
            if event.type == pygame.KEYUP:
                self.released.add(event.key)

            ## Dirty hack
            if event.type == pygame.quit:
                self.pressed.add(pygame.K_ESCAPE)