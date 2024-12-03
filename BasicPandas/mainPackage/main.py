# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

from pandasDemoPackage.pandasDemo import pandasDemo

def demo():
    print("Pandas demo...")
    myPandasDemo = pandasDemo()  # Instantiate an object of type pandasDemo
    myPandasDemo.demo()
    
if __name__ == "__main__":
    demo()