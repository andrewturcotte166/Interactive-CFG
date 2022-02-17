import unittest
from main import CFG

class CFGtest(unittest.TestCase):
    g = CFG()
    g2 = CFG(["A", "B", "C"], ["0", "1", "Є"], {"A": ["0B1", "1C0", "Є"], "B": ["0B1", "Є"], "C": ["1C0", "Є"]}, "A")

    def test_add_variable(self):
        self.assertEqual(CFGtest.g.variables, [], "Should be []")
        CFGtest.g.add_variable("A")
        self.assertEqual(CFGtest.g.variables, ["A"], "Should be [\"A\"]")
        CFGtest.g.add_variable("A")
        CFGtest.g.add_terminal(1)
        CFGtest.g.add_terminal("AA")
        CFGtest.g.add_terminal("~!gd")
        self.assertEqual(CFGtest.g.variables, ["A"], "Should still be [\"A\"]")
        CFGtest.g2.add_variable("D")
        self.assertEqual(CFGtest.g2.variables, ["A", "B", "C", "D"], "Should be [\"A\", \"B\", \"C\", \"D\"]")
        CFGtest.g2.add_variable("0")
        self.assertEqual(CFGtest.g2.variables, ["A", "B", "C", "D"], "Should still be [\"A\", \"B\", \"C\", \"D\"]")

    def test_add_terminal(self):
        self.assertEqual(CFGtest.g.terminals, [], "Should be []")
        CFGtest.g.add_terminal("a")
        self.assertEqual(CFGtest.g.terminals, ["a"], "Should be [\"a\"]")
        CFGtest.g.add_terminal("a")
        CFGtest.g.add_terminal(1)
        CFGtest.g.add_terminal("aa")
        CFGtest.g.add_terminal("~!gd")
        self.assertEqual(CFGtest.g.terminals, ["a"], "Should still be [\"a\"]")
        CFGtest.g2.add_terminal("2")
        self.assertEqual(CFGtest.g2.terminals, ["0", "1", "Є", "2"], "Should be [\"0\", \"1\", \"Є\", \"2\"]")
        CFGtest.g2.add_terminal("A")
        self.assertEqual(CFGtest.g2.terminals, ["0", "1", "Є", "2"], "Should still be [\"0\", \"1\", \"Є\", \"2\"]")

if __name__ == '__main__':
    unittest.main()
