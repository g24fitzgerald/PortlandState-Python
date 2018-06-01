# 12/8/17
# Excerpt From: Bruce A. Tate. “Seven Languages in Seven Weeks (for Gina Fitzgerald).” iBooks.

# “This power-packed class implements a very simple tree.
# It has three methods, initialize, visit, and visit_all,
# and two instance variables, children and node_name.”

#class named in CamelCase
class Tree
  #attr keyword defines an instance variable
  attr_accessor :children, :node_name

  #method 1
  def initialize(name, children=[])

    #prepend instance variables with @
    @children = children
    @node_name = node_name
  end

  #method 2. &block is a reference to the block passed to the method
  def visit_all(&block)
    visit &block
    children.each { |c| c.visit_all &block }
  end

  def visit(&block)
    block.call self
  end
end
