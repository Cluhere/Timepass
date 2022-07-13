def f(root):
  if root==None:
      return
  if root.left and root.right:
      temp=root.left
      root.left=root.right
      root.right=temp
  elif root.left and root.right==None:
      root.right=root.left
      root.left=None
  elif root.right and root.left==None:
      root.left=root.right
      root.right=None

  f(root.left)
  f(root.right)

  f(root)
  return root
