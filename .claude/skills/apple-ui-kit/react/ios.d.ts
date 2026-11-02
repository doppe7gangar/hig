// Types for ios.jsx.
import type { ButtonHTMLAttributes, HTMLAttributes, InputHTMLAttributes, ReactNode,
              RefObject } from "react";

type Div = HTMLAttributes<HTMLElement>;

export function Symbol(p: { name: string; children?: ReactNode } & Div): JSX.Element;
export function NavBar(p: { title?: ReactNode; leading?: ReactNode; trailing?: ReactNode;
  collapsed?: boolean } & Div): JSX.Element;
export function useCollapsed(threshold?: number): boolean;
export function LargeTitle(p: { children: ReactNode } & Div): JSX.Element;
export function Controls(p: { vertical?: boolean; children: ReactNode } & Div): JSX.Element;
export function ControlButton(p: { label: string; symbol?: string; children?: ReactNode }
  & ButtonHTMLAttributes<HTMLButtonElement>): JSX.Element;

export interface TabItem { id: string; label: string; symbol?: string; icon?: ReactNode }
export function TabBar(p: { tabs: TabItem[]; selected: string; onSelect: (id: string) => void;
  label?: string; className?: string }): JSX.Element;

export function List(p: { header?: ReactNode; footer?: ReactNode; children: ReactNode } & Div): JSX.Element;
export function Row(p: { title?: ReactNode; value?: ReactNode; icon?: ReactNode; symbol?: string;
  accessory?: ReactNode; onClick?: () => void; href?: string; chevron?: boolean;
  className?: string; children?: ReactNode }): JSX.Element;

export function Switch(p: { checked: boolean; onChange?: (checked: boolean) => void; label?: string;
  disabled?: boolean } & Omit<InputHTMLAttributes<HTMLInputElement>, "onChange">): JSX.Element;
export function Segmented<T extends string>(p: { options: { value: T; label: ReactNode }[];
  value: T; onChange: (value: T) => void; label: string; className?: string }): JSX.Element;
export function Stepper(p: { value: number; onChange: (value: number) => void; label: string;
  min?: number; max?: number; step?: number }): JSX.Element;
export function Slider(p: { value: number; onChange: (value: number) => void; label: string;
  min?: number; max?: number; step?: number; leading?: ReactNode; trailing?: ReactNode }
  & Omit<InputHTMLAttributes<HTMLInputElement>, "onChange" | "value">): JSX.Element;
export function Field(p: InputHTMLAttributes<HTMLInputElement>): JSX.Element;
export function Button(p: { variant?: "plain" | "filled" | "tinted"; destructive?: boolean;
  wide?: boolean } & ButtonHTMLAttributes<HTMLButtonElement>): JSX.Element;
export function GlassButton(p: { prominent?: boolean; label?: string; symbol?: string }
  & ButtonHTMLAttributes<HTMLButtonElement>): JSX.Element;
export function Chip(p: ButtonHTMLAttributes<HTMLButtonElement>): JSX.Element;
export function PageControl(p: { count: number; index: number; onChange?: (i: number) => void;
  label?: string }): JSX.Element;

export function EmptyState(p: { symbol?: string; icon?: ReactNode; title: ReactNode;
  children?: ReactNode; action?: ReactNode; onAction?: () => void }): JSX.Element;

export interface ModalAction { label: string; role?: "cancel" | "destructive"; onPress?: () => void }
export function Sheet(p: { open: boolean; onClose: () => void; title: ReactNode;
  onConfirm?: () => void; confirmLabel?: string; cancelLabel?: string;
  confirmDisabled?: boolean; children?: ReactNode }): JSX.Element | null;
export function Alert(p: { open: boolean; title: ReactNode; message?: ReactNode;
  actions: ModalAction[]; onClose: () => void }): JSX.Element | null;
export function ActionSheet(p: { open: boolean; title?: ReactNode; message?: ReactNode;
  actions: ModalAction[]; onClose: () => void }): JSX.Element | null;

export function useModal(open: boolean, onClose: () => void, initial?: string): RefObject<HTMLDivElement>;
