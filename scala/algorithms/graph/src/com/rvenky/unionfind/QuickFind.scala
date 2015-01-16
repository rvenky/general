package com.rvenky.unionfind

/**
 * An array of  vertices
 * Initially each inside
 */
class QuickFind(numberVertices: Int) extends UnionFind {

  // initialize arrays to 0 .. n -1 
  private val vertices = (0 to numberVertices - 1) toArray

  /**
   * add a connection a to b
   * for every edge added
   */
  def connect(x: Int, y: Int) =
    {

      val rootx = root(x)
      val rooty = root(y)

      for {
        vertex <- vertices
        if (root(vertex) == rootx)
      } vertices(vertex) = rooty
    }

  def root(index: Int): Int = vertices(index)

  

  def print() :Unit =
    {
    
       println (vertices mkString ("[", " ", "]")) 
      
    }

  // 8-4 0-7 3-7 6-3 1-0 5-9   (quick find)
  // 0-1 9-0 5-4 0-8 3-1 7-6 7-5 7-3 3-2 (quick union)

}