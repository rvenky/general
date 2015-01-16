package com.rvenky.unionfind

trait UnionFind {
  
  def root (x : Int) : Int
  def isConnected (x: Int, y: Int) : Boolean = root(x) == root(y)
  
  
  def connect (x: Int, y: Int) : Unit
  def print () : Unit
  
    def addConnections(edges: List[(Int, Int)]) =
    {
      for ((x, y) <- edges)
        connect(x, y)

    }

}