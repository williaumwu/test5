def default():

    task = {}
    env_vars = []
    shelloutconfigs = []

    shelloutconfigs.append('elasticdev:::ed_core::pre_scripts')
    shelloutconfigs.append('elasticdev:::ed_core::post_scripts')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars, 
                        'shelloutconfigs': shelloutconfigs 
                        }
    return task
