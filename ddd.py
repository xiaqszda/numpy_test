import numpy as np


print(np.eye(4))

dt = np.dtype(
    [('age', 'i1'),
     ('name', 'S20'), ])

print(dt)
a = np.array([('15', 'zhangsna',), (23, 'lisi',), (34, 'wangwu',)], dtype=dt,)
print(a)

x = np.empty([3, 2, 4], dtype=dt)
# print(x.flags)
xx = np.zeros([3, 2, 4], dtype=dt)
# print(xx.flags)
xxx = np.ones([3, 2, 4], dtype=dt)
# print(xxx.flags)

l = [[1, 2, 3], [2, 5, 3]]
ll = np.asarray(l)
# print(l)
# print(ll)

z = np.linspace(21, 22, 10, endpoint=False).reshape(2, 5, 1, 1)
# print(z)
b = np.arange(0, 240, 3).reshape(4, 5, 4)
# print(b)
# print("------------", b[0:2])
d = np.arange(1, 101).reshape(4, 25)
print(d)
print(d[0][10:])
# print(d[10:])
print(d[2, 2])
print(d[d < 5])
print("四个角为:")
print(np.asarray([d[0, 0], d[0, 24], d[3, 0], d[3, 24]]).reshape(2, 2))
row = np.array([[0, 0], [3, 3]])
col = np.array([[0, 24], [0, 24]])
print("and")
print(d[row, col])
print(np.nan)

c = b.reshape(2, 4, 10)
# print(b)
# print(b.ndim)
# print(b.shape)
# print(c)
# print(c.shape)
# print(b)
# b.shape = (3,2,2,10,2)
# print(b)
# print(b.shape)

c = np.logspace(1, 4, 4, base=2)
# print(c)

# x = numpy.array([1,2,3,4,5,6,7,8,9,10])
# print(x)
# print(x.flags)

aa = np.array([np.nan, 1, 2], dtype='f4')
print(aa[~np.isnan(aa)])
print(np.isnan(aa))
print(~np.isnan(aa))
print(True)
print(-False)

cc = np.arange(100).reshape(10, 10)
print(cc)
print(cc[[4, -2, -1]])

print(np.ix_([1, 3, 5], [2, 4, 6]))
print(cc[np.ix_([1, 3, 5], [2, 4, 6])])
print(cc.shape)
aaa = np.array([
    [0, 0, 0],
    [10, 10, 10],
    [20, 20, 20],
    [30, 30, 30]
])
bbb = np.array([0, 1, 2])
print("-----\n", aaa + bbb)
print("-----\n", aaa * bbb)
for i in np.nditer(cc):
    print(i,end=',')
print("\n")
print(cc.T)
for i in np.nditer(cc.copy(order='F'), order='F'):
    print(i,end=',')
print(cc*2)
dd = np.arange(8).reshape(2,4)
for i in np.nditer(dd, op_flags=['readwrite'], order='F'):
    print(i)
    i[...] = i * 2
print(dd)