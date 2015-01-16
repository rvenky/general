package com.rvenky.unionfind

import scala.annotation.tailrec

class QuickUnion(numberVertices: Int) extends UnionFind {

  // initialize arrays to 0 .. n -1 
  private val vertices = (0 to numberVertices - 1) toArray

  private val count = Array.fill(10)(1)

  @tailrec
  final def root(index: Int): Int =
    {
      val maybeRoot = vertices(index)

      if (maybeRoot == index) maybeRoot else root(maybeRoot)

    }

  /*
   * Make root of smaller tree to point to root of larger tree
   */
  
  def connect(x: Int, y: Int): Unit =
    {
      val rootx = root(x)
      val rooty = root(y)
      val countX = count(rootx)
      val countY = count (rooty)
      
      if (countX >= countY) {
        vertices (rooty) = rootx
        count (rootx) += countY
        count (rooty) = 0
      }
      else
      {
        vertices (rootx) = rooty
        count(rooty) += countX
        count (rootx) = 0
      }
      
      println (s"$x, $y")
      print()
      println ()

    }

   def print() :Unit =
    {
       println (vertices mkString ("[", " ", "]"))
    }
   
   

}