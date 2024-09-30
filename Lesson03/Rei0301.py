#例題1 Rei0301.py
#np.arangeとnp.linspace
import numpy as np

print("===========numpy.arange======")
print( f"np.arange(5){np.arange(5)}" )
print( f"np.arange( 0.5 , 4 ){np.arange( 0.5 , 4 )}" )
print( f"np.arange( -3, 3, 0.5 ){np.arange( -3, 3, 0.5 )}" )

print("===========numpy.linspace======")
#0以上10以下を4つ間隔のリスト
print( f"0以上10以下を4つ等間隔のリスト{np.linspace( 0,10,4)}" )
#-1以上1以下を11個の間隔のリスト
print( f"-1以上1以下を11個の等間隔のリスト{np.linspace( -1,1,11)}" )
