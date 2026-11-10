
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from datetime import datetime
from app import assess_risk


# APPLICATION CONFIGURATION
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class RiskAssessmentApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Risk Assessment System")
        #self.geometry("1000x750")
        #self.minsize(900, 680)
        self.geometry("1100x900")
        self.minsize(1000, 800)        
        self.configure(fg_color="#F3F6FA")
        self.entries = []
        self.create_header()
        self.create_main_content()
        self.create_log_section()
        self.create_footer()

    # HEADER
    def create_header(self):

        header = ctk.CTkFrame( self, fg_color="#17365D",
                                corner_radius=0,height=100)

        header.pack(fill="x")
        header.pack_propagate(False)

        title = ctk.CTkLabel( header, text="RISK ASSESSMENT SYSTEM",
                                font=("Arial", 26, "bold"), text_color="white" )

        title.pack(pady=(20, 2))

        subtitle = ctk.CTkLabel( header, text="Patient Risk Classification Application",
                                font=("Arial", 13), text_color="#DCE6F1")

        subtitle.pack()

    
    # TEST CALCULATE BUTTON
    #def test_calculate_click(self):
    #
    #    print("CALCULATE BUTTON CLICKED", flush=True)
    #
    #    self.result_label.configure(
    #        text="BUTTON CLICK REGISTERED",
    #        text_color="#2563EB"
    #    )

    
    # MAIN CONTENT
    def create_main_content(self):
        main_frame = ctk.CTkFrame( self, fg_color="transparent" )

        main_frame.pack( fill="x", padx=35, pady=1)

        main_frame.configure(height=515)
        main_frame.pack_propagate(False)
        # INPUT PANEL
        input_panel = ctk.CTkFrame( main_frame, fg_color="white",
                                    corner_radius=12)

        input_panel.pack( side="left", fill="both", expand=True,
                        padx=(0, 15) )

        ctk.CTkLabel( input_panel, text="Patient Feature Input",
                        font=("Arial", 20, "bold"), text_color="#17365D"
                        ).pack(pady=(16, 4))

        ctk.CTkLabel( input_panel, 
                     text="Enter the five features required by the model.",
                    font=("Arial", 12), text_color="#64748B").pack(pady=(0, 8))

        # FIVE INPUT FIELDS
        for i in range(5):
            field_frame = ctk.CTkFrame( input_panel, fg_color="transparent")
            field_frame.pack( fill="x", padx=30, pady=2 )

            label = ctk.CTkLabel( field_frame, text=f"Feature {i + 1}",
                                    font=("Arial", 13, "bold"), 
                                    text_color="#334155", anchor="w")

            label.pack(anchor="w", pady=(0, 5))

            entry = ctk.CTkEntry( field_frame, height=30,
                                    placeholder_text=f"Enter feature {i + 1}",
                                    font=("Arial", 13), border_color="#CBD5E1",
                                    fg_color="#F8FAFC", text_color="#1E293B" )

            entry.pack(fill="x")

            # Allow mouse clicking and keyboard focus
            #entry.configure(state="normal")
            
            self.entries.append(entry)

        # BUTTONS
        button_frame = ctk.CTkFrame( input_panel, fg_color="transparent" )

        button_frame.pack(pady=(10,5))

        calculate_button = ctk.CTkButton( button_frame, text="CALCULATE RISK",
                                            width=170, height=38, 
                                            font=("Arial", 13, "bold"),
                                            fg_color="#2563EB", hover_color="#1D4ED8",
                                            command=self.calculate_risk
                                            #command=self.test_calculate_risk
                                            )

        calculate_button.pack( side="left", padx=8 )

        clear_button = ctk.CTkButton( button_frame, text="CLEAR", width=110,
                                        height=38, font=("Arial", 13, "bold"),
                                        fg_color="#64748B", hover_color="#475569",
                                        command=self.clear_fields)

        clear_button.pack( side="left", padx=8 )

        # RESULT PANEL
        result_panel = ctk.CTkFrame( main_frame, fg_color="white",
                                        corner_radius=12, width=300 )

        result_panel.pack( side="right", fill="both", padx=(15, 0))

        result_panel.pack_propagate(False)

        ctk.CTkLabel( result_panel, text="Assessment Result",
                        font=("Arial", 20, "bold"),
                        text_color="#17365D").pack(pady=(25, 20))

        self.sum_label = ctk.CTkLabel( result_panel, text="Model Value: --",
                                        font=("Arial", 14), text_color="#475569" )

        self.sum_label.pack(pady=15)

        self.result_label = ctk.CTkLabel( result_panel, text="AWAITING INPUT",
                                            font=("Arial", 19, "bold"),
                                            text_color="#64748B", wraplength=250)

        self.result_label.pack(pady=25)

        ctk.CTkLabel( result_panel,
                        text="Results are generated using\nthe existing assessment model.",
                        font=("Arial", 11), text_color="#94A3B8",
                        justify="center").pack(pady=10)

    # ASSESSMENT LOG
    def create_log_section(self):
        log_panel = ctk.CTkFrame( self, fg_color="white", corner_radius=12)
        log_panel.pack( fill="both", expand=True, padx=30, pady=(5, 15))
    # LOG HEADER
        log_header = ctk.CTkFrame( log_panel, fg_color="transparent" )

        log_header.pack( fill="x", padx=20, pady=10 )

        ctk.CTkLabel( log_header, text="Assessment History Log",
                        font=("Arial", 18, "bold"), text_color="#17365D"
                    ).pack(side="left")

        ctk.CTkButton( log_header, text="CLEAR LOG", width=110,
                        height=28, fg_color="#DC2626",
                        hover_color="#B91C1C", command=self.clear_log
                    ).pack(side="right")

        # TABLE HEADER
        table_header = ctk.CTkFrame( log_panel, fg_color="#E8EEF5",
                                    height=35, corner_radius=5 )

        table_header.pack( fill="x", padx=20, pady=(0, 5))

        table_header.pack_propagate(False)

        table_header.grid_columnconfigure(0, weight=3)
        table_header.grid_columnconfigure(1, weight=2)
        table_header.grid_columnconfigure(2, weight=3)

        headers = ["Timestamp", "Model Value", "Classification"]

        for col, text in enumerate(headers):
            ctk.CTkLabel( table_header, text=text,
                            font=("Arial", 12, "bold"),
                            text_color="#334155", anchor="w"
                        ).grid( row=0, column=col, sticky="ew",
                        padx=12)

        # SCROLLABLE LOG
        self.log_container = ctk.CTkScrollableFrame( log_panel,
                                                    fg_color="white",
                                                    corner_radius=5)

        self.log_container.pack( fill="both", expand=True, padx=20,
                                 pady=(0, 15))

        self.log_placeholder = ctk.CTkLabel( self.log_container,
                                            text="No assessment records available.",
                                            font=("Arial", 12), text_color="#94A3B8")

        self.log_placeholder.pack(pady=25)

        self.log_count = 0
    
    # CALCULATE RISK
    def calculate_risk(self):
        try:
            numbers = []
            # Read and validate five features
            for index, entry in enumerate(self.entries):

                value_text = entry.get().strip()

                if not value_text:
                    messagebox.showerror( "Invalid Input",
                                            f"Please enter Feature {index + 1}.")
                    entry.focus_set()
                    return

                value = float(value_text)

                if not (float("-inf") < value < float("inf")):
                    raise ValueError( f"Feature {index + 1} must be a finite number.")

                numbers.append(value)

            # Run assessment model
            total = sum(numbers)
            result = assess_risk(numbers)

            # Determine classification
            if result == "RISK":
                classification = "HIGH RISK"
                color = "#DC2626"
            else:
                classification = "LOW RISK"
                color = "#16A34A"

            # Update result immediately
            self.sum_label.configure( text=f"Model Value: {total:g}" )

            self.result_label.configure( text=classification, text_color=color )

            # Add assessment to log
            self.add_log_entry(total, classification)

            # Refresh GUI
            self.update_idletasks()

        except ValueError as error:

            messagebox.showerror( "Invalid Input", str(error) )

        except Exception as error:

            messagebox.showerror( "Assessment Error", str(error))
    
    # ADD LOG ENTRY
    def add_log_entry(self, total, classification):

        if self.log_count == 0:
            self.log_placeholder.destroy()

        timestamp = datetime.now().strftime( "%Y-%m-%d %H:%M:%S" )

        row = ctk.CTkFrame( self.log_container, fg_color="#F1F5F9",
                            corner_radius=5, height=42 )

        row.pack( fill="x", pady=3 )

        row.pack_propagate(False)

        # Configure columns
        row.grid_columnconfigure(0, weight=3)
        row.grid_columnconfigure(1, weight=2)
        row.grid_columnconfigure(2, weight=3)

        # Timestamp
        ctk.CTkLabel( row, text=timestamp, font=("Arial", 11),
                        text_color="#475569", anchor="w" ).grid(
                        row=0, column=0, sticky="ew", padx=12)

        # Model value
        ctk.CTkLabel( row, text=f"{total:g}", font=("Arial", 11),
                        text_color="#475569", anchor="w"
                        ).grid( row=0, column=1, sticky="ew", padx=12)

        # Classification
        result_color = ( "#DC2626"
                    if classification == "HIGH RISK"
                        else "#16A34A")

        ctk.CTkLabel( row, text=classification, font=("Arial", 11, "bold"),
                        text_color=result_color, anchor="w"
                    ).grid( row=0, column=2, sticky="ew", padx=12)

        self.log_count += 1

        print( f"Log entry added: {timestamp} | "
                f"{total:g} | {classification}",
                flush=True)

        # Refresh and scroll to latest entry
        self.after( 100,
                    lambda: self.log_container._parent_canvas.yview_moveto(1.0))

    # CLEAR INPUT FIELDS
    
    def clear_fields(self):
        #Clear fields
        for entry in self.entries:
            entry.delete(0, "end")
        # Reset model values
        self.sum_label.configure( text="Model Value: --" )

        self.result_label.configure( text="AWAITING INPUT",
                                        text_color="#64748B" )

        # Return focus to the first input field
        #self.after(100, self.focus_first_entry)

    
    # CLEAR HISTORY LOG
    
    def clear_log(self):

        if self.log_count == 0:
            return

        confirm = messagebox.askyesno( "Clear History",
                            "Are you sure you want to clear the assessment history?",
                                        parent=self )

        if confirm:
            for widget in self.log_container.winfo_children():
                widget.destroy()

            self.log_count = 0

            self.log_placeholder = ctk.CTkLabel( self.log_container,
                                                text="No assessment records available.",
                                                font=("Arial", 12), text_color="#94A3B8" )

            self.log_placeholder.pack(pady=25)

            # Refresh the log container
            self.log_container.update_idletasks()
            
        # Restore normal window activation
        self.after(200, self.restore_window)

    def restore_window(self):
        if self.winfo_exists():
            self.lift()

            # Return keyboard focus to the window,
            # without forcing focus onto an input field.
            self.focus_set()   
    # FOOTER

    def create_footer(self):

        footer = ctk.CTkLabel( self,
                                text="Risk Assessment System | Powered by Python",
                                font=("Arial", 10), text_color="#94A3B8" )
        footer.pack(pady=(0, 10))


# RUN APPLICATION

if __name__ == "__main__":

    application = RiskAssessmentApp()
    application.mainloop()
