import gc
import inspect
import sys

def gcCheck():

    gc.collect()

    found_bugger = False
    currentframe = inspect.currentframe()

    print(60 * '=')
    print('Performing garbage check')
    print(60 * '=')

    for o in gc.get_objects():
        try:
            repr(o)
            continue
        except SystemError as ex:
            print('Found one: %x = %s' % (id(o), ex))
        except RuntimeError as ex:
            print('Found one: %x = %s' % (id(o), ex))

        print('Referrers are:')
        for ref in gc.get_referrers(o):
            if ref is currentframe:
                continue

            try:
                print('    - %x (%x) = %r' % (id(ref), sys.getrefcount(ref), ref))
            except Exception as ex:
                print('    - %x (%x) = (dead proxy %r)' % (id(ref), sys.getrefcount(ref), str(ex)))

        print('Referents are:')
        for ref in gc.get_referents(o):
            # There are a lot of references to ints; don't print those.
            # Feel free to remove this and see the whole list, though.
            if isinstance(ref, int):
                continue
            
            try:
                print('    - %x (%x) = %r' % (id(ref), sys.getrefcount(ref), ref))
            except Exception as ex:
                print('    - %x (%x) = (dead proxy %r)' % (id(ref), sys.getrefcount(ref), str(ex)))

        found_bugger = True

    if not found_bugger:
        print('Found nothing wrong.')

if __name__ == '__main__':
    do_garbage_check()
