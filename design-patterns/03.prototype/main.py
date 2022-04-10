from classes import ProblemTicket, Prototype

pr = ProblemTicket(
    name = 'Test ticket',
    description = 'Problem record description',
    labels = ['Test cloning', 'Service down'],
    priority = 'High',
    reporter = 'Jordan'
    )


prototype = Prototype()
prototype.register('pr1', pr)

pr_clone_1 = prototype.clone('pr1')

print(id(pr))
print(id(pr_clone_1))