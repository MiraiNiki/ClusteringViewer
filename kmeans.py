# coding:utf-8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#calclate k-means clustering
#input: array of point
#output: array consist of color number(start with 1)
import math

testArray = [[100,0], [0,3], [0,6], [3,0], [3,3], [3,6]]

def createNewCenterPoints(numOfCluster):
	cp = []
	for i in range(numOfCluster):
		cp.append([0,0])
	return cp

#def createCenterPoints():
def getColor(pointArray, centerPoints, numOfCluster):
	color = 0
	cArray = []
	for i in range(len(pointArray)):
		minDistance = 9223372036854775807
		cArray.append(0)
		for j in range(len(centerPoints)):
			dx = float(pointArray[i][0]) - float(centerPoints[j][0])
			dy = float(pointArray[i][1]) - float(centerPoints[j][1])
			distance = pow(dx, 2) + pow(dy, 2)
			if distance < minDistance: # and cArray.count(j+1) < (len(pointArray) / numOfCluster):
				minDistance = distance
				cArray[i] = j + 1
	#print(cArray)
	return cArray

def copyColor(colorArray, preColorArray):
	for i in range(len(colorArray)):
		preColorArray[i] = colorArray[i]

def checkColorChanged(colorArray, preColorArray):
	for i in range(len(colorArray)):
		if int(colorArray[i]) != int(preColorArray[i]):
			return True
	print("NotChange")
	return False

def calcKmeans(pointArray, numOfCluster):
	centerPoints = createNewCenterPoints(numOfCluster)
	#step1 ランダムにクラスタを割り当てる
	resultArray = []
	colorArray = []
	preColorArray = []
	for i in range(len(pointArray)):
		colorArray.append(i%numOfCluster + 1)
		preColorArray.append(0)
	#print(colorArray)
	cnt = 0
	while(checkColorChanged(colorArray, preColorArray) == True and cnt < 100):
		#print(cnt)
		cnt = cnt + 1
		copyColor(colorArray, preColorArray)
		#step2 割り振ったデータのクラスタ毎に中心を計算
		for i in range(len(pointArray)):
			centerPoints[colorArray[i] - 1][0] = 0
			centerPoints[colorArray[i] - 1][1] = 0
		for i in range(len(pointArray)):
			centerPoints[colorArray[i] - 1][0] = centerPoints[colorArray[i] - 1][0] + pointArray[i][0] * numOfCluster / len(pointArray)
			centerPoints[colorArray[i] - 1][1] = centerPoints[colorArray[i] - 1][1] + pointArray[i][1] * numOfCluster / len(pointArray)
		#step3 各座標とクラスタの中心との距離を求め、カラーを変更する
		colorArray = getColor(pointArray, centerPoints, numOfCluster)
		resultArray.append(colorArray)
		#print(resultArray)
	return resultArray
		
result = calcKmeans(testArray, 3)
#print(result)