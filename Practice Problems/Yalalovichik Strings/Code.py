
for _ in range(int(input())):
	n,s = int(input()),input().strip()
	previ,num,_s,dic = s[0],0,[],{}
	for i in s:
		if previ == i:
			num+=1
			continue
		_s.append((previ, num))
		if previ not in dic or dic[previ]<num:dic[previ] = num
		previ,num = i,1
	_s.append((previ, num))
	if previ not in dic or dic[previ]<num:dic[previ] = num
	sum1 = sum(dic.values())
	del dic, s
	l,dicc = [i for (i, j) in _s],{}
	congr = [(l[i], l[i+1]) for i in range(len(l)-1)]
	for i in range(len(congr)):
		if congr[i] not in dicc:dicc[congr[i]] = set()
		dicc[congr[i]].add( (_s[i][1], _s[i+1][1]) )       
	sum2,ll = 0,[]
	for i in dicc.keys():
		sortedset,deleted =  sorted(list(dicc[i])),[]
		for k in range(1, len(sortedset)):
			j = sortedset[k]         
			if j[1]>sortedset[k-1][1]:
				ind = k - 1
				while ind>=0 and j[1]>=sortedset[ind][1]:
					deleted.append(ind)
					ind = ind-1
			elif j[1]==sortedset[k-1][1]:deleted.append(k-1)
			elif j[0]==sortedset[k-1][0] and j[1]<sortedset[k-1][1]:deleted.append(k)
		dicc[i],prevx,thissum = sorted(list(set(sortedset) - {sortedset[i] for i in deleted}), key = lambda x: x[0]),0,0
		for j in dicc[i]:
			x, y = j
			thissum+=(x - prevx)*(y)
			prevx = x
		sum2+=thissum
		ll.append((i, thissum))
	ll.sort(key = lambda x: x[0] )
	print((sum1+sum2))	# cook your dish here
