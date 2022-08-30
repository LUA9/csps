import js2py

substr = js2py.eval_js(
    '''
    function substr(string, start, end) {
        return string.substr(start, end)
    }
    '''
)

match_school_ra = js2py.eval_js(
    '''
    function match_school_ra(string) {
        return string.match(/url:'.(.*?)'/) 
    }
    '''
)

match_sc_data = js2py.eval_js(
    '''
    function match_sc_data(string) {
        return string.match(/\(.*?\)/)
    }
    '''
)

resolve_sc_data = js2py.eval_js(
    '''
    function resolve_sc_data(string) {
        return string.replace(/[()]/g, '').replace(/'/g, '').split(',')
    }
    '''
)

buffer_to_string = js2py.eval_js(
    '''
    function buffer_to_string(buffer) {
        return buffer.toString(16)
    }
    '''
)

last_index_of = js2py.eval_js(
    '''
    function last_index_of(string, search_string) {
        return string.lastIndexOf(search_string)
    }
    '''
)
