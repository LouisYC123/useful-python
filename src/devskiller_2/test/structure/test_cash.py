import base64
import unittest

import app.cash


class StructureTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.MODULE = app.cash

    def test_class_exists_cash(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )

    def test_class_function_exists_cash___abs__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2Fic19f").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2Fic19f').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___abs__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2Fic19f").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2Fic19f').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2Fic19f").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2Fic19f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2Fic19f").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2Fic19f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )

    def test_class_function_exists_cash___add__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2FkZF9f").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2FkZF9f').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___add__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2FkZF9f").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2FkZF9f').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2FkZF9f").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2FkZF9f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2FkZF9f").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2FkZF9f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2FkZF9f").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"b3RoZXI=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2FkZF9f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`other`.",
        )

    def test_class_function_exists_cash___bool__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2Jvb2xfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2Jvb2xfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___bool__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2Jvb2xfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2Jvb2xfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2Jvb2xfXw==").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2Jvb2xfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2Jvb2xfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2Jvb2xfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )

    def test_class_function_exists_cash___eq__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2VxX18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2VxX18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___eq__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2VxX18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2VxX18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2VxX18=").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2VxX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2VxX18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2VxX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2VxX18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"b3RoZXI=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2VxX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`other`.",
        )

    def test_class_function_exists_cash___ge__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2dlX18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2dlX18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___ge__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2dlX18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2dlX18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2dlX18=").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2dlX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2dlX18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2dlX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2dlX18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"b3RoZXI=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2dlX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`other`.",
        )

    def test_class_function_exists_cash___gt__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2d0X18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2d0X18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___gt__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2d0X18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2d0X18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2d0X18=").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2d0X18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2d0X18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2d0X18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2d0X18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"b3RoZXI=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2d0X18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`other`.",
        )

    def test_class_function_exists_cash___init__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2luaXRfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2luaXRfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___init__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2luaXRfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2luaXRfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            3,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 3 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"YW1vdW50").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`amount`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"Y3VycmVuY3k=").decode(),
            args[2],
            msg=f"The argument #2 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`currency`.",
        )

    def test_class_function_exists_cash___le__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2xlX18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2xlX18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___le__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2xlX18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2xlX18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2xlX18=").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2xlX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2xlX18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2xlX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2xlX18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"b3RoZXI=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2xlX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`other`.",
        )

    def test_class_function_exists_cash___lt__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2x0X18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2x0X18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___lt__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX2x0X18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2x0X18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2x0X18=").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX2x0X18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2x0X18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2x0X18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX2x0X18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"b3RoZXI=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX2x0X18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`other`.",
        )

    def test_class_function_exists_cash___ne__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX25lX18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX25lX18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___ne__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX25lX18=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX25lX18=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX25lX18=").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX25lX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX25lX18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX25lX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX25lX18=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"b3RoZXI=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX25lX18=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`other`.",
        )

    def test_class_function_exists_cash___neg__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX25lZ19f").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX25lZ19f').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___neg__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX25lZ19f").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX25lZ19f').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX25lZ19f").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX25lZ19f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX25lZ19f").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX25lZ19f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )

    def test_class_function_exists_cash___pos__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX3Bvc19f").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX3Bvc19f').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___pos__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX3Bvc19f").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX3Bvc19f').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX3Bvc19f").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX3Bvc19f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX3Bvc19f").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX3Bvc19f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )

    def test_class_function_exists_cash___radd__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX3JhZGRfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX3JhZGRfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___radd__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX3JhZGRfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX3JhZGRfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX3JhZGRfXw==").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX3JhZGRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX3JhZGRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX3JhZGRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX3JhZGRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"b3RoZXI=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX3JhZGRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`other`.",
        )

    def test_class_function_exists_cash___repr__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX3JlcHJfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX3JlcHJfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash___repr__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fX3JlcHJfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX3JlcHJfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX3JlcHJfXw==").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fX3JlcHJfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fX3JlcHJfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fX3JlcHJfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )

    def test_class_function_exists_cash__get_amount(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fZ2V0X2Ftb3VudA==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fZ2V0X2Ftb3VudA==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash__get_amount(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC5fZ2V0X2Ftb3VudA==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fZ2V0X2Ftb3VudA==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fZ2V0X2Ftb3VudA==").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC5fZ2V0X2Ftb3VudA==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fZ2V0X2Ftb3VudA==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC5fZ2V0X2Ftb3VudA==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC5fZ2V0X2Ftb3VudA==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"b3RoZXI=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2FzaC5fZ2V0X2Ftb3VudA==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`other`.",
        )

    def test_class_function_exists_cash_to(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC50bw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC50bw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_cash_to(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2FzaA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2FzaA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2FzaC50bw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC50bw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC50bw==").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2FzaC50bw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC50bw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2FzaC50bw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2FzaA==").decode(),
            base64.b64decode(b"Q2FzaC50bw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"dGFyZ2V0X2N1cnJlbmN5").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2FzaC50bw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2FzaA==').decode()}` "
            f"should be called "
            f"`target_currency`.",
        )

    def test_class_exists_targetcurrency(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"VGFyZ2V0Q3VycmVuY3k=").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'VGFyZ2V0Q3VycmVuY3k=').decode()}` "
            f"is not found, but it was marked as required.",
        )


# === Internal functions, do not modify ===
import inspect

from types import ModuleType
from typing import List


def _get_function_names(module: ModuleType) -> List[str]:
    names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            names.append(name)
    return names


def _get_function_arg_names(module: ModuleType, fn_name: str) -> List[str]:
    arg_names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            if fn.__qualname__ == fn_name:
                args_spec = inspect.getfullargspec(fn)
                arg_names = args_spec.args
                if args_spec.varargs is not None:
                    arg_names.extend(args_spec.varargs)
                if args_spec.varkw is not None:
                    arg_names.extend(args_spec.varkw)
                arg_names.extend(args_spec.kwonlyargs)
                break
    return arg_names


def _get_class_names(module: ModuleType) -> List[str]:
    names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for name, cls in classes:
        if cls.__module__ == module.__name__:
            names.append(name)
    return names


def _get_class_function_names(module: ModuleType, cls_name: str) -> List[str]:
    fn_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name, fn in functions:
                    fn_names.append(fn.__qualname__)
                break
    return fn_names


def _get_class_function_arg_names(
    module: ModuleType, cls_name: str, fn_name: str
) -> List[str]:
    arg_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name_, fn in functions:
                    if fn.__qualname__ == fn_name:
                        args_spec = inspect.getfullargspec(fn)
                        arg_names = args_spec.args
                        if args_spec.varargs is not None:
                            arg_names.extend(args_spec.varargs)
                        if args_spec.varkw is not None:
                            arg_names.extend(args_spec.varkw)
                        arg_names.extend(args_spec.kwonlyargs)
                        break
                break
    return arg_names
