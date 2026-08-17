#!/usr/bin/env python3
import re
from pathlib import Path

SCSS_PATH = Path(__file__).resolve().parent.parent / "_sass" / "_home.scss"
OUTPUT_PATH = Path(__file__).resolve().parent / "home.css"

var_pattern = re.compile(r"\$[a-zA-Z0-9_-]+")

class Node:
    def __init__(self, kind, selector=None):
        self.kind = kind  # 'root', 'rule', 'at-rule'
        self.selector = selector
        self.children = []
        self.declarations = []

    def add_child(self, node):
        self.children.append(node)

    def add_declaration(self, name, value):
        self.declarations.append((name, value))


def parse_scss(text):
    text = re.sub(r"//.*", "", text)
    root = Node("root")
    stack = [root]
    variables = {}

    buffer = ""

    def current_node():
        return stack[-1]

    def handle_declaration(raw):
        raw = raw.strip()
        if not raw:
            return
        if raw.endswith(";"):
            raw = raw[:-1].rstrip()
        if not raw:
            return
        if raw.startswith("$"):
            if ":" not in raw:
                return
            name, value = raw.split(":", 1)
            variables[name.strip()] = value.strip()
            return
        if ":" not in raw:
            return
        name, value = raw.split(":", 1)
        current_node().add_declaration(name.strip(), value.strip())

    def handle_open(token):
        token = token.strip()
        if not token:
            return
        if token.startswith("@"):
            node = Node("at-rule", token)
        else:
            selectors = [sel.strip() for sel in token.split(",") if sel.strip()]
            node = Node("rule", selectors)
        current_node().add_child(node)
        stack.append(node)

    def handle_close():
        if len(stack) == 1:
            return
        stack.pop()

    for ch in text:
        if ch == '{':
            token = buffer
            buffer = ""
            handle_open(token)
        elif ch == '}':
            handle_declaration(buffer)
            buffer = ""
            handle_close()
        elif ch == ';':
            buffer += ch
            handle_declaration(buffer)
            buffer = ""
        else:
            buffer += ch

    return root, variables


def replace_variables(value, variables):
    def repl(match):
        return variables.get(match.group(0), match.group(0))
    return var_pattern.sub(repl, value)


def emit_node(node, variables, parent_selectors=None, indent=0):
    parent_selectors = parent_selectors or []
    lines = []

    if node.kind == "root":
        for child in node.children:
            lines.extend(emit_node(child, variables, parent_selectors, indent))
        return lines

    if node.kind == "at-rule":
        lines.append(" " * indent + f"{node.selector} {{")
        for child in node.children:
            lines.extend(emit_node(child, variables, parent_selectors, indent + 2))
        lines.append(" " * indent + "}")
        return lines

    # rule
    if parent_selectors:
        combined = []
        for parent in parent_selectors:
            parent = parent.strip()
            for child_sel in node.selector:
                child_sel = child_sel.strip()
                if not parent:
                    combined.append(child_sel)
                elif child_sel.startswith(":") or child_sel.startswith("::"):
                    combined.append(f"{parent}{child_sel}")
                elif child_sel.startswith((">", "+", "~")):
                    combined.append(f"{parent} {child_sel}")
                else:
                    combined.append(f"{parent} {child_sel}")
    else:
        combined = node.selector

    selectors_text = ", ".join(combined)
    lines.append(" " * indent + f"{selectors_text} {{")
    for name, value in node.declarations:
        resolved_value = replace_variables(value, variables)
        lines.append(" " * (indent + 2) + f"{name}: {resolved_value};")
    lines.append(" " * indent + "}")

    for child in node.children:
        lines.extend(emit_node(child, variables, combined, indent))

    return lines


def compile_scss_to_css():
    text = SCSS_PATH.read_text()
    root, variables = parse_scss(text)
    lines = emit_node(root, variables)
    OUTPUT_PATH.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    compile_scss_to_css()
