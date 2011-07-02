import codecs

from jspy.parser import Parser
from jspy.js import Console, ExecutionContext, UNDEFINED


__version__ = '1.0'


def create_default_global_objects():
    return {'console': Console()}


def eval_file(file_name, global_objects=None):
    if global_objects is None:
        global_objects = create_default_global_objects()

    # Parse file
    with codecs.open(file_name, encoding='utf-8') as f:
        file_contents = f.read()
    program = Parser().parse(file_contents)
    declared_vars = dict((name, UNDEFINED) for name in program.get_declared_vars())
    declared_vars.update(global_objects)

    # Create the execution context object
    context = ExecutionContext(declared_vars)

    # Run code
    result = program.eval(context)
    return result.value, context


def _main():
    import argparse

    parser = argparse.ArgumentParser(description="Execute a single JavaScript file.")
    parser.add_argument("source", metavar="SOURCE", help="Source file to execute")
    parser.add_argument('-c', '--context', action='store_true', dest='dump_context', default=False,
                      help='Dump execution context after running the file')
    args = parser.parse_args()

    # Run the file
    result, final_context = eval_file(args.source)
    print 'Result: %r' % result

    if args.dump_context:
        print
        print 'Context:'
        print '--------'
        print
        
        for name, value in sorted(context.env.iteritems()):
            print '%s: %r' % (name, value)

