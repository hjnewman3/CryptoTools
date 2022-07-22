from fastapi import APIRouter
from typing import Optional

router = APIRouter(
  prefix='/inverse',
  tags=['inverse']
)

@router.get("/")
def inverse(x, n, showTable: Optional[str] = None):
  qi = [0]
  ri = []
  si = [1, 0]
  ti = [0, 1]
  i = 1
  i_count = [0, 1]

  while x != 0:
    i += 1
    i_count.append(i)

    q = n // x
    qi.append(q)

    n, x = x, n % x
    ri.append(x)

    s = si[i_count[i-2]] - qi[i_count[i-1]] * si[i_count[i-1]]
    si.append(s)

    t = ti[i_count[i-2]] - qi[i_count[i-1]] * ti[i_count[i-1]]
    ti.append(t)

  i_count = i_count[2:]
  qi = qi[1:]
  si = si[2:]
  ti = ti[2:]
  
  if showTable is not None:
    print('{0: ^5}'.format('i'), '{0: ^5}'.format('qi-1'), '{0: ^5}'.format('ri'), '{0: ^5}'.format('si'), '{0: ^5}'.format('ti'))
    print('{0: ^5}'.format('-----'), '{0: ^5}'.format('-----'), '{0: ^5}'.format('-----'), '{0: ^5}'.format('-----'), '{0: ^5}'.format('-----'))
    for k in range(len(i_count)):
        print('{0: ^5}'.format(i_count[k]), '{0: ^5}'.format(qi[k]), '{0: ^5}'.format(ri[k]), '{0: ^5}'.format(si[k]), '{0: ^5}'.format(ti[k]))

    print('\ninverse:', ti[len(ti)-2])
    return None

  #return ti[len(ti)-2]
  return { 'Inverse': f'{ti[len(ti)-2]}' }