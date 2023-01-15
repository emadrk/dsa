package trees.trees_java.anujtutorials.lec57;

import java.util.Scanner;

public class HeightBinaryTree {
    static Scanner sc = null;
    public static void main(String[] args) {
        System.out.println("hi");
        sc = new Scanner(System.in);

        Node root = createtree();
        // System.out.println("preorder");
        // preOrderTraversal(root);

        // System.out.println();
        // System.out.println("inorder");
        // inOrder(root);

        // System.out.println();
        // System.out.println("postorder");
        // postOrder(root);
        System.out.println("height->"+heightBinaryTree(root));

        
    }
    static int heightBinaryTree(Node root){
        if(root==null){
            return 0;
        }
        return Math.max(heightBinaryTree(root.left),heightBinaryTree(root.right))+1;
    }
    static Node createtree() {
        Node root = null;
        System.out.println("Enter data: ");
        int data = sc.nextInt();

        if (data==-1){
            return null;
        }
        root = new Node(data);
        System.out.println("Enter left for "+data);
        root.left = createtree();

        System.out.println("Enter right for "+data);
        root.right = createtree();

        return root;
    }

    static void preOrderTraversal(Node root){
        if(root==null){

            return;
        }
        System.out.print(root.data);
        preOrderTraversal(root.left);
        preOrderTraversal(root.right);
        return;
    }

    static void inOrder(Node root){
        if (root == null){
            return;
        }
        inOrder(root.left);
        System.out.print(root.data);
        inOrder(root.right);

        return;
    }

    static void postOrder(Node root){
        if (root == null){

            return;
        }
        postOrder(root.left);
        postOrder(root.right);
        System.out.print(root.data);

        return;
    }



}

class Node{
    Node left,right;
    int data;

    public Node(int data){
        this.data=data;
    }
}

