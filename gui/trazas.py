import trace

tracer = trace.Trace(count=True, trace=True)
tracer.run('inicio.py')
results = tracer.results()
results.write_results(show_missing=True, coverdir='.')
print(results)